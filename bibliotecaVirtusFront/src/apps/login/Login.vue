<template>
    <div class="login-container">
      <h1>Login</h1>
      <form @submit.prevent="submitForm">
        <div>
          <label for="firstName">Nome:</label>
          <input type="text" id="firstName" v-model="user.firstName" required>
        </div>
  
        <div>
          <label for="lastName">Sobrenome:</label>
          <input type="text" id="lastName" v-model="user.lastName" required>
        </div>
  
        <div>
          <label for="email">E-mail:</label>
          <input type="email" id="email" v-model="user.email" required>
        </div>
  
        <div>
          <label for="password">Senha:</label>
          <input type="password" id="password" v-model="user.password" required>
        </div>
  
        <div>
          <label for="confirmPassword">Confirmação de Senha:</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required>
        </div>
  
        <div v-if="passwordMismatch">
          <p>A senha e a confirmação de senha não são iguais.</p>
        </div>
  
        <button type="submit">Entrar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginPage',
    data() {
      return {
        user: {
          firstName: '',
          lastName: '',
          email: '',
          password: '',
        },
        confirmPassword: '',
        passwordMismatch: false
      };
    },
    methods: {
      submitForm() {
        if (this.user.password !== this.confirmPassword) {
          this.passwordMismatch = true;
        } else {
          this.passwordMismatch = false;
          // Aqui você pode adicionar a lógica de submissão do formulário, como uma requisição HTTP
          console.log('Form submitted:', this.user);
        }
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
  