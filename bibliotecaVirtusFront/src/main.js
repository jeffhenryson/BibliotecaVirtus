import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js'; // Garanta que o caminho esteja correto
import store from './store/Vuex'; // Adicione esta linha para importar seu Vuex store

const app = createApp(App);
app.use(router); // Primeiro, usa-se o Vue Router
app.use(store);  // Depois, aplica-se o Vuex store
app.mount('#app');
