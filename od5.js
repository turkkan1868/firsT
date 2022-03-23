const Koa = require('koa');
const Router = require('@koa/router');

const app = new Koa();
const router = new Router();

router.get('/', (ctx) => {
  ctx.body = '<h1>INDEX </h1>'
});

router.get('/about', (ctx) => {
    ctx.body = '<h1>HAKKIMDA</h1>'
  });

  router.get('/contact', (ctx) => {
    ctx.body = '<h1>ILETISIM </h1>'
  });

app.use(router.routes())
const port = 3000;

  app.listen(3000,() => {
      console.log(`app started on port ${port}`)
  })
