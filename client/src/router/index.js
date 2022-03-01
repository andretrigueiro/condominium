import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Adm from '../views/AdmView.vue';
import Resident from '../views/ResidentView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/adm',
    name: 'Adm',
    component: Adm,
  },
  {
    path: '/resident',
    name: 'Resident',
    component: Resident,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
