<template>
  <div class="home">
    <h1 v-if="username">Seja Bem-vindo, {{ username }} ao Nosso Mundo Digital!</h1>
    <h1 v-else>Seja Bem-vindo(a) ao Nosso Mundo Digital!</h1>
    <p>Explorar, aprender e se conectar nunca foi tão fácil. Aqui, no <strong>Meu Projeto Vue</strong>, nós trabalhamos
      incansavelmente para trazer a você uma experiência digital única e enriquecedora. Navegue pelo nosso site para
      descobrir ferramentas inovadoras, conteúdos exclusivos e uma comunidade vibrante pronta para te receber de braços
      abertos.</p>
    <p>Seja buscando novos conhecimentos, compartilhando suas experiências ou apenas explorando o que temos a oferecer,
      você está no lugar certo. Bem-vindo à jornada que começa agora. Estamos ansiosos para caminhar ao seu lado.</p>

      <button @click="getRandomNumber">Obter Número</button>
      <p v-if="randomNumberMessage" class="messageNumber">{{ randomNumberMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import { emitter } from '@/eventBus';

export default {
  name: 'HomePage',
  data() {
    return {
      randomNumberMessage: null
    };
  },
  computed: {
    username() {
      return localStorage.getItem('username');
    }
  },
  methods: {
    userLoggedInHandler() {
      console.log('Usuário logado, atualizando componente.');
      this.$forceUpdate();
    },
    async getRandomNumber() {
      try {
        const username = this.username;
        const response = await axios.get(`http://localhost:8000/number`, { params: { username } });
        this.randomNumberMessage = response.data.message;
      } catch (error) {
        console.error('Erro ao obter o número aleatório:', error);
        this.randomNumberMessage = 'Não foi possível obter um número. Tente novamente.';
      }
    }
  },
  mounted() {
    emitter.on('user-logged-in', this.userLoggedInHandler);
  },
  unmounted() {
    emitter.off('user-logged-in', this.userLoggedInHandler);
  }
};
</script>

  
<style>
  .home button {
    background-color: #4CAF50; /* Green */
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border: none;
    border-radius: 4px;
  }

  .messageNumber {
    background-color: #f2f2f2;
    padding: 10px;
    border-left: 3px solid #4CAF50;
    margin-top: 20px;
  }

.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f5f5f5;
  color: #333;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #2c3e50;
  font-size: 2.5em;
  margin-bottom: 0.5em;
}

p {
  color: #34495e;
  font-size: 1.2em;
  line-height: 1.6;
  max-width: 600px;
  margin-bottom: 1em;
}

strong {
  color: #2980b9;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2em;
  }

  p {
    font-size: 1em;
  }
}
</style>
  