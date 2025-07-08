<script setup>

const {incompletedTodos, completedTodos} = defineProps(['incompletedTodos', 'completedTodos'])

</script>


<template>
<div class="p-4 mx-20 w-5/6 h-svh bg-white rounded-t-2xl shadow-md">
        <ul class="w-4/6 mx-auto">
                <li v-for="(todo, index) in incompletedTodos" class="mt-2 px-2 pb-1.5 border-b-2 border-gray-100 flex justify-between group relative">
                    <div class="absolute left-[-15px] top-[15%] text-gray-100 group-hover:text-gray-400">

                            <button @click="$emit('todo-completed', todo.id)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
                                    <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425z"/>
                                </svg>
                            </button>

                    </div>
                    <p v-text="todo.message"></p>
                </li>

                    <li v-for="todo in completedTodos" class="mt-2 px-2 pb-1.5 border-b-2 border-gray-100 flex justify-between group relative">
                        <div class="absolute left-[-15px] top-[15%] text-gray-100 group-hover:text-gray-400">

                                <button @click="$emit('todo-delete', todo.id)">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">
                                        <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
                                    </svg>
                                </button>

                        </div>
                        <p v-text="todo.message" class="text-gray-300"></p>
                    </li>
        </ul>
    </div>
    </template>