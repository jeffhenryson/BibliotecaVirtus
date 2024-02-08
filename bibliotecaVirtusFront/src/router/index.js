import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/home/Home.vue";
import Login from "../apps/login/Login.vue";
import Signup from "../apps/signup/Signup.vue";
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
