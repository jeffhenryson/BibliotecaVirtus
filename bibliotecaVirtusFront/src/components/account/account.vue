<template>
    <div class="account">
      <h1>Minha Conta</h1>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    name: 'AccountPage', // Modificado para seguir a regra de nomes de componentes de múltiplas palavras
    setup() {
      const title = ref('Minha Conta');
  
      return {
        title,
      };
    },
  };
  </script>
  
  <style scoped>
  .account {
    /* Estilizações */
  }
  </style>
  