<template>
  <div class="home">
    <h1>Bem-vindo ao Meu Projeto Vue</h1>
    <p>Esta é a página inicial do aplicativo. Aqui você pode colocar informações sobre o aplicativo ou sobre a sua empresa.</p>
    <button @click="goToLogin">Login</button>
    <button @click="goToSignup">Cadastro</button>
  </div>
</template>
  
  <script>
  export default {
    name: 'HomePage',
    methods: {
      goToLogin() {
        // Adicione a lógica para ir para a página de Login
        this.$router.push('/login');
      },
      goToSignup() {
        // Adicione a lógica para ir para a página de Cadastro
        this.$router.push('/signup');
      }
    }
  };
  </script>
  
  <style scoped>
  .home {
    text-align: center;
    margin-top: 50px;
  }
  
  button {
    margin: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  </style>
  