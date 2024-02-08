import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js'; // Garanta que o caminho esteja correto

const app = createApp(App);
app.use(router);
app.mount('#app');
