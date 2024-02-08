<template>
  <div class="login-container">
    <h1>Login</h1>
    <form @submit.prevent="submitForm">

      <div>
        <label for="email">E-mail:</label>
        <input type="email" id="email" v-model="user.email" required>
      </div>

      <div>
        <label for="password">Senha:</label>
        <input type="password" id="password" v-model="user.password" required>
      </div>

      <button type="submit">Entrar</button>
    </form>
  </div>
</template>

  
<script>
import axios from 'axios'; // Importe o axios

export default {
  name: 'LoginPage',
  data() {
    return {
      user: {
        email: '', // Removido firstName e lastName pois não são mais usados
        password: '',
      },
      confirmPassword: '', // Se não estiver usando, pode remover
      passwordMismatch: false // Se não estiver usando, pode remover
    };
  },
  methods: {
    submitForm() {
      // Supondo que não precisa mais da lógica de confirmPassword
      axios.post('http://127.0.0.1:8000/login', this.user)
        .then(response => {
          // Trate a resposta aqui
          console.log('Success:', response);
          // Redirecione o usuário ou mostre uma mensagem de sucesso
        })
        .catch(error => {
          // Trate o erro aqui
          console.error('Error:', error.response);
          // Mostre uma mensagem de erro, se necessário
        });
    }
  }
};
</script>
  
  <style scoped>
  .login-container {
    max-width: 300px;
    margin: 50px auto;
    padding: 20px;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .login-container div {
    margin-bottom: 10px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  button {
    padding: 10px 20px;
    cursor: pointer;
  }
  
  p {
    color: red;
  }
  </style>
  