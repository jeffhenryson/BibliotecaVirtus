// Importe `createStore` do Vuex 4 em vez de `Vue` e `Vuex`
import { createStore } from "vuex";
import axios from "axios";

// Use `createStore` em vez de `Vue.use(Vuex)` e `new Vuex.Store`
export default createStore({
  state: {
    isAuthenticated: false,
    username: null,
    token: null,
  },
  mutations: {
    SET_USER_DATA(state, { username, token }) {
      console.log("Atualizando estado com:", username, token); // Adicione este log
      state.isAuthenticated = true;
      state.username = username;
      state.token = token;
      localStorage.setItem("user", JSON.stringify({ username, token }));
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    },
    CLEAR_USER_DATA(state) {
      state.isAuthenticated = false;
      state.username = null;
      state.token = null;
      localStorage.removeItem("user");
      axios.defaults.headers.common["Authorization"] = null;
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post(
          "http://localhost:8000/login",
          credentials
        );
        const { access_token, username } = response.data;
        commit("SET_USER_DATA", { username, token: access_token });
        console.log("Login successful");
      } catch (error) {
        throw new Error(
          "Erro ao fazer login: " +
            (error.response.data.detail || error.message)
        );
      }
    },
    logout({ commit }) {
      commit("CLEAR_USER_DATA");
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    username(state) {
      return state.username;
    },
    token(state) {
      return state.token;
    },
  },
});
