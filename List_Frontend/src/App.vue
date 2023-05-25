<script setup lang="ts">
</script>
<template>
  <div id="app">
    <header>
      <div class="Lista">
        <div class="Listbox">
          <h1>Lista de Compras</h1>
        </div>
      </div>
    </header>
    <main>
      <Login v-if="!loggedIn && !showRegister" @login-success="loginSuccess" @go-to-register="showRegister = true" />
      <Register v-if="!loggedIn && showRegister" @register-success="loginSuccess" @go-to-login="showRegister = false" />
      <div class="task-container" v-if="loggedIn">
        <task-list ref="taskList" />
      </div>
    </main>
  </div>
</template>

<script>
import Login from './components/Login.vue'
import Register from './components/Register.vue';
import TaskList from './components/TaskList.vue';
export default {
  name: 'App',
  components:{
    Login,
    Register,
    TaskList,
  },
  data() {
    return {
      loggedIn: false,
      showRegister: false,
    };
  },
  methods: {
    loginSuccess(userId) {
    this.loggedIn = true;
    this.$nextTick(() => {
      this.$refs.taskList.loadTasks(userId);
    });
  },
  },
};
</script>
<style>
.Lista{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0%;
}
.Listbox{
  border-radius: 10px;
}
h1{
font-family: 'Times New Roman', Times, serif;
text-align: center;
color: white;
background: rgba( 0, 0, 0, 0.5 );
box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
backdrop-filter: blur( 20px );
-webkit-backdrop-filter: blur( 20px );
border-radius: 10px;
border: 1px solid rgba( 255, 255, 255, 0.18 );
}
body{
  background-image: url('./assets/teste.jpg');
  background-size: 100vw 100vh;
}

</style>
