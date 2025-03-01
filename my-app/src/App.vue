<template>
  <nav>
    <router-link to="/">Главная</router-link>
    <router-link to="/about">О нас</router-link>
  </nav>
  <router-view />
</template>

<style>
nav {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
</style>