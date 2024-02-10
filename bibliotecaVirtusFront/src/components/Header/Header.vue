<template>
  <header class="header">
    <nav>
      <router-link to="/">Home</router-link>
      <template v-if="userLoggedIn">
        <div class="relative" @click="toggleDropdown">
          <button class="text-white bg-blue-500 hover:bg-blue-700 font-medium py-2 px-4 rounded inline-flex items-center">
            <span>Conta</span>
          </button>
          <div v-if="showDropdown" class="absolute right-0 mt-2 py-2 w-48 bg-white rounded-md shadow-xl z-20">
            <router-link to="/account" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-500 hover:text-white">Conta</router-link>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-500 hover:text-white" @click.prevent="logout">Logout</a>
          </div>
        </div>
      </template>
      <template v-else>
        <router-link to="/login">Login</router-link>
        <router-link to="/signup">Cadastro</router-link>
      </template>
    </nav>
  </header>
</template>

<script>
import { emitter } from '@/eventBus';

export default {
  name: 'AppHeader',
  data() {
    return {
      showDropdown: false,
    };
  },
  computed: {
    userLoggedIn() {
      return !!localStorage.getItem('access_token');
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('username');
      // Emitir evento de logout
      emitter.emit('user-logged-out');
      this.$router.push('/login');
      this.showDropdown = false;
    },
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    }
  },
  mounted() {
    emitter.on('user-logged-in', () => this.$forceUpdate());
    emitter.on('user-logged-out', () => this.$forceUpdate());
  },
  unmounted() {
    emitter.off('user-logged-in');
    emitter.off('user-logged-out');
  }
};
</script>

  
<style scoped>
.header {
  background-color: #343a40;
  color: white;
  padding: 20px 20px;
  text-align: center;
}

.header nav {
  display: flex;
  justify-content: center;
  align-items: center;
}

.header nav a {
  color: white;
  margin: 0 10px;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.header nav a:hover {
  color: #1abc9c;
}

/* Estilo para o botão que ativa o menu dropdown */
.header .relative button {
  cursor: pointer;
  border: none;
  outline: none;
  background-color: #3498db;
  color: white;
  padding: 10px 15px;
  border-radius: 5px;
  transition: background-color 0.3s ease-in-out;
}

.header .relative button:hover {
  background-color: #2980b9;
}

/* Estilo para o menu dropdown */
.header .relative .absolute {
  display: none;
  position: absolute;
  right: 0;
  background-color: white;
  color: black;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  z-index: 1;
  border-radius: 5px;
}

.header .relative .absolute a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.header .relative .absolute a:hover {
  background-color: #f1f1f1;
}

/* Mostrando o menu dropdown quando showDropdown é true */
.header .relative:hover .absolute {
  display: block;
}

.header nav a:first-of-type {
  margin-right: 650px;
  margin-left: 650px;
}
</style>

  