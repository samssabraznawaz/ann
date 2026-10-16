"""Navigation test of SaNaSoft-ANN (index.html): the Home link is at the top and at the bottom,
the logo leads to the app's own start (Welcome step), and work is kept when the user goes to the
start page and comes back in the same tab.

    SANASOFT_LIBS=<folder with local libraries> python tests/e2e/test_nav.py
"""
import asyncio, functools, http.server, os, pathlib, sys, threading
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    handler = functools.partial(Quiet, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


async def main():
    srv = serve()
    url = f'http://127.0.0.1:{srv.server_address[1]}/index.html'
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1400, 'height': 1000})
        libs = os.environ.get('SANASOFT_LIBS')
        if libs:
            for pat, f in [('**/papaparse.min.js', 'papaparse.min.js'), ('**/xlsx.full.min.js', 'xlsx.full.min.js'), ('**/chart.umd.min.js', 'chart.umd.min.js')]:
                await page.route(pat, (lambda path: lambda r: r.fulfill(path=path, content_type='text/javascript'))(os.path.join(libs, f)))
            await page.route('**/fonts.googleapis.com/**', lambda r: r.abort())
        # the real start page is on the internet; answer it locally so the round trip can be tested offline
        await page.route('https://sanapls.com/**', lambda r: r.fulfill(body='<title>start</title><p>start page</p>', content_type='text/html'))
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        await page.goto(url)
        await page.wait_for_function("typeof Papa !== 'undefined'", timeout=30000)

        top = page.locator('nav.suitebar a.sb-home')
        bottom = page.locator('footer.suitefoot a.sb-home')
        assert await top.count() == 1 and await bottom.count() == 1, 'Home link missing at top or bottom'
        assert (await top.inner_text()).strip() == 'Home' and (await bottom.inner_text()).strip() == 'Home'
        assert await top.get_attribute('href') == 'https://sanapls.com/'
        assert await bottom.get_attribute('href') == 'https://sanapls.com/'
        assert await page.locator('nav.suitebar a[aria-current]').inner_text() == 'ANN'

        await page.evaluate('loadDemo()')
        await page.evaluate('goStep(4)')
        title = await page.title()
        assert 'ANN' in title, title

        # logo -> the app's own start (Welcome), the data stays loaded
        await page.click('#homebtn')
        assert await page.evaluate('APP.step') == 0
        assert await page.evaluate('!!(APP.data && APP.data.rows.length)'), 'data lost after the logo click'
        await page.evaluate('goStep(4)')

        # Home (top) -> start page -> Back: same step, same data
        await top.click()
        await page.wait_for_url('https://sanapls.com/**')
        await page.go_back()
        await page.wait_for_function("typeof APP !== 'undefined' && APP.step === 4", timeout=30000)
        assert await page.evaluate('APP.data.rows.length') > 0

        # Home (bottom) works the same way
        await page.evaluate('goStep(3)')
        await bottom.click()
        await page.wait_for_url('https://sanapls.com/**')
        await page.go_back()
        await page.wait_for_function("typeof APP !== 'undefined' && APP.step === 3", timeout=30000)

        # no "preview", "test" or "trial" wording on the screen
        body = (await page.inner_text('body')).lower()
        for w in ['preview', 'trial', 'testing phase', 'beta']:
            assert w not in body, f'found "{w}"'
        await browser.close()
    srv.shutdown()
    if errors:
        print('JavaScript errors:', errors)
        sys.exit(1)
    print('NAV OK')

asyncio.run(main())
