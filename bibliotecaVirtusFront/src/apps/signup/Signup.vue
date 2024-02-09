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
/* Reset básico para remover estilos padrão do navegador */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body, html {
  height: 100%;
  margin: 0;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  background: #f0f2f5; /* Cor de fundo mais moderna e suave */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Estilização do Container */
.signup-container {
  width: 100%;
  max-width: 450px;
  background: #ffffff;
  padding: 2rem;
  margin: 1rem;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
}

/* Estilização dos Grupos de Formulário */
.form-group label {
  font-size: 1rem;
  color: #333;
  margin-bottom: 0.5rem;
  display: block;
  text-align: left;
}

/* Estilização dos Inputs */
input[type="text"],
input[type="email"],
input[type="password"] {
  font-size: 1rem;
  padding: 0.75rem;
  border: 1px solid #dcdfe4;
  border-radius: 8px;
  width: 100%;
  transition: all 0.3s;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
  outline: none;
  border-color: #8aaae5;
  box-shadow: 0 0 0 3px rgba(138, 170, 229, 0.2);
}

/* Estilização do Botão de Enviar */
.btn-submit {
  padding: 1rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  background-image: linear-gradient(45deg, #06b, #06f);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  width: 100%;
  margin-top: 1rem;
}

.btn-submit:hover,
.btn-submit:focus {
  background-image: linear-gradient(45deg, #058, #05f);
}

/* Mensagens de Erro e Sucesso */
.error-message p,
.success-message p {
  font-size: 0.875rem;
  padding: 0.75rem;
  border-radius: 8px;
  margin-top: 1rem;
  text-align: left;
}

.error-message p {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.success-message p {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

/* Responsividade */
@media (max-width: 768px) {
  .signup-container {
    padding: 1.5rem;
    margin: 0.5rem;
  }

  .btn-submit {
    padding: 0.75rem 1rem;
  }
}

/* Adicione mais estilos responsivos conforme necessário */

</style>