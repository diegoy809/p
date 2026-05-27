const CACHE_NAME = 'patente-ab-v3';

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
  // API和字体请求直接放行，绝不缓存拦截
  if (e.request.url.includes('api.anthropic.com') ||
      e.request.url.includes('googleapis.com') ||
      e.request.url.includes('gstatic.com')) {
    e.respondWith(fetch(e.request));
    return;
  }
  // app资源：缓存优先
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
