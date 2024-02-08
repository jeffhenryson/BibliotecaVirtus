<template>
  <header class="header">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/signup">Cadastro</router-link>
    </nav>
  </header>
</template>
  
<script>
export default {
  name: 'AppHeader'
};
</script>
  
<style scoped>
.header {
  background-color: #343a40;
  color: white;
  padding: 10px 20px;
  text-align: center;
}

.header a {
  color: white;
  margin: 0 10px;
  text-decoration: none;
}
</style>
  