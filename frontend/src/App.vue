<script setup>
import Header from "@/components/Header.vue"
import InputField from "@/components/InputField.vue"
import DisplayTodos from "@/components/DisplayTodos.vue"
import {ref, onMounted} from 'vue';
import axios from "axios";

const incompletedTodos = ref([])
const completedTodos = ref([])


async function fetchData(){
    const res = await axios.get("http://127.0.0.1:5000/todos")
    const data = await res.data
    incompletedTodos.value = data["incompleted_todos"]
    completedTodos.value = data["completed_todos"]
}

fetchData()

async function addTodo(inputValue){
    await axios.post("http://127.0.0.1:5000/todos",{
        "todo": inputValue
    })
    await fetchData()
}

async function todosCompleted(id){
    await axios.post("http://127.0.0.1:5000/todos/complete",{
        "id" : id
    })
    await fetchData()
}

async function todoDeleted(id){
    await axios.post("http://127.0.0.1:5000/todos/delete",{
        "id" : id
    })
    await fetchData()
}


</script>

<template>

    <Header />
    <InputField @add-todo="addTodo"/>
    <DisplayTodos :incompletedTodos="incompletedTodos" :completedTodos="completedTodos" 
    @todo-completed="todosCompleted" @todo-delete="todoDeleted"/>

</template>

<style scoped></style>
