<template>
  <div class="container">
    <div class="signup-container">
      <h1>Cadastro</h1>
      <form @submit.prevent="submitForm">

        <div class="form-group">
          <label for="username">Nome de Usuário:</label>
          <input type="text" id="username" placeholder="Exemplo: johndoe" v-model="user.username" required>
        </div>
        <br>
        <div class="form-group">
          <label for="firstName">Nome:</label>
          <input type="text" id="firstName" placeholder="Exemplo: John" v-model="user.firstName" required>
        </div>
        <br>
        <div class="form-group">
          <label for="secondName">Sobrenome:</label>
          <input type="text" id="secondName" placeholder="Exemplo: Doe" v-model="user.secondName" required>
        </div>
        <br>
        <div class="form-group">
          <label for="email">E-mail:</label>
          <input type="email" id="email" placeholder="Exemplo: john.doe@example.com" v-model="user.email" required>
        </div>
        <br>
        <div class="form-group">
          <label for="password">Senha:</label>
          <input type="password" id="password" placeholder="Crie uma senha" v-model="user.password" required>
        </div>
        <br>
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
    <div class="image-container">
      <img src="../../assets/independent-bookstore-day.jpg" alt="Descrição da imagem" />
    </div>
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

body,
html {
  height: 100%;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  background: linear-gradient(135deg, #b8faff 0%, #e8fdff 70%, #a69785 100%);
  /* Gradiente de fundo conforme solicitado */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: #665c49;
  /* Cor de texto principal com base na paleta fornecida */
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
  color: #665c49;
  /* Cor de texto secundário */
  margin-bottom: 1 0px;
  display: block;
  text-align: left;
}

/* Estilização dos Inputs */
input[type="text"],
input[type="email"],
input[type="password"] {
  font-size: 1rem;
  padding: 0.75rem;
  border: 1px solid #ced4da;
  border-radius: 8px;
  width: 100%;
  transition: all 0.3s;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  /* Efeito de sombra ao redor dos inputs */
}

input[type="text"],
input[type="email"],
input[type="password"] {
  font-size: 1rem;
  padding: 0.75rem;
  border: 1px solid #ced4da;
  border-radius: 8px;
  width: 100%;
  transition: all 0.3s;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  /* Efeito de sombra interna nos inputs */
}

/* Placeholder Styles */
::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #a0a0a0;
  opacity: 1;
  /* Firefox */
  font-style: italic;
}

:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: #a0a0a0;
  font-style: italic;
}

::-ms-input-placeholder {
  /* Microsoft Edge */
  color: #a0a0a0;
  font-style: italic;
}

/* Estilização do Botão de Enviar */
.btn-submit {
  padding: 1rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  background-color: #665c49;
  /* Botão com cor baseada na paleta fornecida */
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
  background-color: #a69785;
  /* Efeito hover com outra cor da paleta */
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

.container {
  display: flex; /* Cria um layout flexível */
  align-items: stretch; /* Alinha verticalmente */
  justify-content: center; /* Alinha horizontalmente */
  gap: 0; 
  margin-left: 300px/* Sem espaço entre os elementos filho */
}

/* Estilo do container do formulário */
.signup-container {
  /* As mesmas regras de estilo que você já tem */
  margin-right: 0; /* Remove a margem direita, se houver */
}

.signup-container,
.image-container {
  flex: 1; /* Faz com que o formulário e a imagem ocupem proporções iguais no container */
  display: flex; /* Permite mais controle sobre o conteúdo interno */
  flex-direction: column; /* Organiza o conteúdo interno em uma coluna */
  justify-content: center; /* Centraliza o conteúdo interno verticalmente */
}

/* Estilo do container da imagem */
.image-container img {
  width: 100%; /* Garante que a imagem ocupe todo o espaço disponível na largura */
  height: 100%; /* Garante que a imagem ocupe todo o espaço disponível na altura */
  object-fit: cover; /* Garante que a imagem cubra o espaço sem distorção */
}

/* Estilo da imagem */
.image-container img {
  width: 50%;
  height: 95%; /* Mantém a proporção da imagem */
  display: block; /* Remove espaços extras */
  border-radius: 12px; /* Arredonda os cantos se desejar */
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