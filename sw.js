const CACHE_NAME = 'patente-ab-v2';

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(c => c.addAll(['./', './index.html', './manifest.json']))
  );
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  // API请求直接放行，不缓存
  if (e.request.url.includes('api.anthropic.com') ||
      e.request.url.includes('fonts.google')) {
    e.respondWith(fetch(e.request));
    return;
  }
  // 其他资源缓存优先
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
