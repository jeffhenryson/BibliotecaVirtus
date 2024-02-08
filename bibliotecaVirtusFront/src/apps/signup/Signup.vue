<template>
  <div class="signup-container">
    <h1>Cadastro</h1>
    <form @submit.prevent="submitForm">

      <div class="form-group">
        <label for="username">Nome de Usuário:</label>
        <input type="text" id="username" v-model="user.username" required>
      </div>

      <div class="form-group">
        <label for="firstName">Primeiro Nome:</label>
        <input type="text" id="firstName" v-model="user.firstName" required>
      </div>

      <div class="form-group">
        <label for="secondName">Segundo Nome:</label>
        <input type="text" id="secondName" v-model="user.secondName" required>
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

      <div v-if="passwordError" class="error-message">
        <p>A senha deve ter pelo menos 6 caracteres, incluir uma letra maiúscula, um número e um símbolo.</p>
      </div>

      <div v-if="emailError" class="error-message">
        <p>O e-mail está com o domínio errado</p>
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
        username: '',
        firstName: '',
        secondName: '',
        email: '',
        password: '',
      },
      confirmPassword: '',
      passwordMismatch: false,
      emailError: false,
      passwordError: false,
    };
  },
  methods: {
    validatePassword(password) {
      const minLength = password.length >= 6;
      const hasUpperCase = /[A-Z]/.test(password);
      const hasNumber = /\d/.test(password);
      const hasSymbol = /[!@#$%^&*(),.?":{}|<>]/.test(password);
      return minLength && hasUpperCase && hasNumber && hasSymbol;
    },
    async submitForm() {

      this.passwordError = !this.validatePassword(this.user.password);
      if (this.emailError || this.passwordMismatch || this.passwordError) {
        return;
      }
      
      if (!this.emailError && !this.passwordMismatch && !this.passwordError) {
        const userData = {
          username: this.user.username,
          primeiro_nome: this.user.firstName,
          segundo_nome: this.user.secondName,
          email: this.user.email,
          password: this.user.password,
        };
        
        try {
          const response = await fetch('http://127.0.0.1:8000/cadastro', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
          });

          if (!response.ok) {
            throw new Error('Algo deu errado com o pedido de cadastro');
          }

          this.$router.push('/');

        } catch (error) {
          console.error('Erro ao enviar o formulário:', error);
        }
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