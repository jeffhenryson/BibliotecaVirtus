<template>
    <div class="signup-container">
      <h1>Cadastro</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="firstName">Nome:</label>
          <input type="text" id="firstName" v-model="user.firstName" required>
        </div>
  
        <div class="form-group">
          <label for="lastName">Sobrenome:</label>
          <input type="text" id="lastName" v-model="user.lastName" required>
        </div>
  
        <div class="form-group">
          <label for="email">E-mail:</label>
          <input type="email" id="email" v-model="user.email" required>
        </div>
  
        <div class="form-group">
          <label for="password">Senha:</label>
          <input type="password" id="password" v-model="user.password" required>
        </div>
  
        <div class="form-group">
          <label for="confirmPassword">Confirme a Senha:</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required>
        </div>
  
        <div v-if="passwordMismatch" class="error-message">
          <p>As senhas não coincidem!</p>
        </div>
  
        <button type="submit" class="btn-submit">Cadastrar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SignupPage',
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
          // Limpar formulário ou redirecionar usuário
        }
      }
    }
  };
  </script>
  
  <style scoped>

.signup-container {
  max-width: 300px;
  margin: 50px auto;
  padding: 20px;
  text-align: center;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 15px;
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
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn-submit {
  padding: 10px 20px;
  width: 100%;
  border-radius: 5px;
  cursor: pointer;
  background-color: #5cb85c;
  color: white;
  border: 1px solid #4cae4c;
}

.error-message p,
.success-message p {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
  padding: 10px;
  border-radius: 5px;
}

.success-message p {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}

  </style>