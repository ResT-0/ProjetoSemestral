<template>
  <div>
    <div class="teste">
    <form @submit.prevent="addList">
      <div class="registro">
      <input type="text" v-model="newList.item" id="item" placeholder="Digite um item" required />
      <input type="number" v-model="newList.num" id="num" placeholder="Digite a quantidade" required />
      <select  v-model="newList.uni" name="unidade" id="unidade" required >
        <option value="unidade">Unidade</option>
        <option value="quilos">quilos</option>
        <option value="gramas">gramas</option>
        <option value="litros">Litros</option>
        <option value="mililitro">mililitro</option>
      </select>
      <button type="submit">Adicionar</button>
    </div> 
    </form>
    <ul>
  <li v-for="task in tasks" :key="task._id">
    <div class="List-description">
      {{ task.description }}
    </div>
    <div class="List-quantidade">
      {{ task.number }}
      {{ task.unidade }}
    </div>
    <div class="List-actions">
      <button @click="deleteList(task._id)">Excluir</button>
      <button @click="showUpdateTaskForm(task)" style="margin-left: 10px;">Atualizar</button>
    </div>
    <div v-if="taskBeingEdited && taskBeingEdited._id === task._id">
      <h3>Editar Item</h3>
      <form @submit.prevent="updateTaskAndHideForm" class="update">
        <input type="text" v-model="taskBeingEdited.description" required style="background-color: lightgray"/>
        <input type="number" v-model="taskBeingEdited.number" required style="background-color: lightgray"/>
        <select  v-model="taskBeingEdited.unidade" name="unidade" id="unidade" required >
        <option value="unidade">Unidade</option>
        <option value="quilos">quilos</option>
        <option value="gramas">gramas</option>
        <option value="litros">Litros</option>
        <option value="mililitro">mililitro</option>
      </select>
        <button type="submit">Salvar</button>
        <button type="button" @click="taskBeingEdited = null">Cancelar</button>
      </form>
    </div>
  </li>
</ul>

  </div>
</div>
</template>

<script>
import { getList, createList, updatelist, deleteList} from "../api";

export default {
  data() {
    return {
      tasks: [],
      newList:{
        item: "",
        num: "",
        uni: "",
      },
      taskBeingEdited: null,
      userId: null,
    };
  },
  methods: {
    async loadTasks(userId) {
      this.userId = userId;
      this.tasks = await getList(userId);
    },
    async addList() {
      const task = {
        description: this.newList.item,
        number: this.newList.num,
        unidade: this.newList.uni,
        done: false,
      };
      const createdList = await createList(task, this.userId);
      this.tasks.push(createdList);
    },
    async deleteList(taskId) {
      await deleteList(taskId);
      this.tasks = this.tasks.filter((task) => task._id !== taskId);
    },
    showUpdateTaskForm(task) {
      this.taskBeingEdited = task;
  },
    async updateTaskAndHideForm() {
      await updatelist(this.taskBeingEdited._id, this.taskBeingEdited);
      this.taskBeingEdited = null;
  },
  },
};
</script>

<!-- Add your scoped styles here -->

<style scoped>
* {
  margin: 0%;
  box-sizing: border-box;
}

div {
  font-family: 'Times New Roman', Times, serif;;
}

h2, h3 {
  color: #333;
  margin-bottom: 1rem;  /* adicionado para dar espaço entre o título e o formulário abaixo */
}

form {
  text-align: center;
  margin-left: 0%;
  justify-content: center;
}

input, select {
  flex:0;
  margin-bottom: 0.5rem; /* Adiciona isso para dar espaço entre os elementos do formulário */
  border: none;
  border-radius: 5px;
  text-align: center;
  background-color:lightgrey;
}

input, select {
  flex-grow: 1;
  padding: 0.6rem 0.5rem; /* Adicione um pouco mais de padding vertical */
  margin-bottom: 0.5rem; /* Adiciona isso para dar espaço entre os elementos do formulário */
  border: none;
  border-radius: 5px;
}

button {
  padding: 0.5rem 1rem;
  background:aliceblue;
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 0.5rem;
}

button:hover {
  background-color: grey;
}
ul{
  display: flex;
  height: 50vh;
  justify-content: center;
  align-items: center;
  margin: 0%;
  flex-wrap: wrap;
  padding-left: 0px;
}
li {
  font-size: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  background: rgba( 98, 98, 98, 0.75 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 20px );
  -webkit-backdrop-filter: blur( 20px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  padding: 1rem;
  border-radius: 5px;
  margin-bottom: 1.5rem;
  flex-basis: calc(20% - 1rem); /* faz com que a task ocupe um terço da largura total, descontando a margem */
  margin-left: 45px;
}
.update {
  display: flex;
  flex-direction: column;
  margin: 0%;
}
.List-description {
  margin-bottom: 0.25rem;
  background-color: lightgray;
  border-radius: 10px;
}

.List-actions {
  display: flex;   
  flex-direction: row;  
  justify-content: center; 
}
.List-quantidade{
  margin-bottom: 0.25rem;
  background-color: lightgray;
  border-radius: 10px;
  margin-bottom: 10px;
}
h3{
  color: black;
}
</style>

