
<template>
  <div class="login">
    <div class="box">
      <h2 style="text-align: center;">Login</h2>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Username" required style="margin-bottom: 5%; margin-left: 20%;"/>
        <input type="password" v-model="password" placeholder="Password" required style="margin-bottom: 5% ;margin-left: 20%;" /><br>
        <button type="submit" style="margin-bottom:5% ;margin-left: 20%;">Login</button>
      </form>
      <button @click="$emit('go-to-register')" style="margin-left: 20%;">Registrar</button>
    </div>
  </div>
</template>

<script>
  import { loginUser } from "../api";
  
  export default {
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      async login() {
        try {
          const user = {
            username: this.username,
            password: this.password,
          };
          const userId = await loginUser(user); // Armazenar o retorno da chamada
          this.$emit('login-success', userId);  // Emitir o userId no evento
        } catch (error) {
          console.error(error);
          alert('Login falhou');
        }
      },
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.login {
display: flex;
height: 50vh;
justify-content: center;
align-items: center;
margin: 0%;
}
.box {
width: 300px;
height: 300px;
background: rgba( 98, 98, 98, 0.75 );
box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
backdrop-filter: blur( 20px );
-webkit-backdrop-filter: blur( 20px );
border: 1px solid rgba( 255, 255, 255, 0.18 );
border-radius: 10px;
}
body{
  margin: 0%;
}
button {
  padding: 0.5rem 1rem;
  background:aliceblue;
  color: black;
  border: none;
  align-items: center;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 0.5rem;
  margin-left: 45px;
}
input{
  flex:0;
  margin-bottom: 0.5rem; /* Adiciona isso para dar espaço entre os elementos do formulário */
  border: none;
  border-radius: 5px;
  text-align: center;
  background-color: aliceblue;
}
</style>
