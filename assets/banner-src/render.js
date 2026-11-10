// Renders ../banner.png, ../banner_cn.png, ../banner_ja.png and ../banner_ko.png.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2560, height: 800 } });
  for (const l of ['en', 'cn', 'ja', 'ko']) {
    await p.goto('file://' + path.join(__dirname, 'banner.html') + '#' + l);
    await p.reload();
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(1500);
    await p.screenshot({ path: path.join(__dirname, '..', l === 'en' ? 'banner.png' : 'banner_' + l + '.png') });
  }
  await b.close();
})();
