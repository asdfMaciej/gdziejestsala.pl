import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App);

app.provide('$debug', import.meta.env.VITE_DEBUG == 'true' ? true : false);

app.use(createPinia());
app.use(router);

app.mount('#app');
