<template>
  <div class="signup-container">
    <h1>Cadastro</h1>
    <form @submit.prevent="submitForm">

      <div class="form-group">
        <label for="username">Nome de Usuário:</label>
        <input type="text" id="username" v-model="user.username" required>
      </div>

      <div class="form-group">
        <label for="firstName">Nome:</label>
        <input type="text" id="firstName" v-model="user.firstName" required>
      </div>

      <div class="form-group">
        <label for="secondName">Sobrenome:</label>
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

      <div v-if="emailError" class="error-message">
        <p>{{ emailErrorMessage || "O e-mail está com o domínio errado" }}</p>
      </div>

      <div v-if="usernameError" class="error-message">
        <p>{{ usernameErrorMessage }}</p>
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
      usernameError: false, // Adicionado para o erro de nome de usuário
      usernameErrorMessage: '', // Mensagem de erro personalizada para nome de usuário
      passwordMismatch: false,
      emailError: false,
      passwordError: false,
      emailErrorMessage: '',
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
    validateEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailPattern.test(email);
    },
    async submitForm() {
      this.passwordMismatch = this.user.password !== this.confirmPassword;
      this.emailError = !this.validateEmail(this.user.email);
      this.passwordError = !this.validatePassword(this.user.password);
      this.emailErrorMessage = '';
      this.usernameError = false;
      this.usernameErrorMessage = '';

      if (this.emailError || this.passwordMismatch || this.passwordError) {
        return;
      }

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
          const responseBody = await response.json(); // Obter o corpo da resposta
          if (response.status === 400) {
            if (responseBody.detail === 'Username already registered') {
              this.usernameError = true;
              this.usernameErrorMessage = "Nome de usuário já existe. Escolha outro nome.";
            } else if (responseBody.detail === 'Email already registered') {
              this.emailError = true;
              this.emailErrorMessage = "E-mail já cadastrado. Faça login ou insira outro e-mail.";
            } else {
              throw new Error('Algo deu errado com o pedido de cadastro');
            }
          } else {
            throw new Error('Algo deu errado com o pedido de cadastro');
          }
        } else {
          this.$router.push('/');
        }
      } catch (error) {
        console.error('Erro ao enviar o formulário:', error);
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