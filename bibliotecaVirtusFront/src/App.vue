<template>
  <div id="app">
    <AppHeader/>
    <router-view/>
  </div>
</template>

<script>
import AppHeader from './components/Header/Header.vue'

export default {
  name: 'App',
  components: {
    AppHeader
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box; /* Isso garante que padding e border não aumentem o tamanho dos elementos */
}
</style>
