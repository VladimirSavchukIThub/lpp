<template>
  <div class="container">
    <h1 class="title">Добавить чек</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label>Имя:</label>
        <input v-model="name" type="text" required />
      </div>

      <div class="form-group">
        <label>Сумма:</label>
        <input v-model="amount" type="number" required />
      </div>

      <div class="form-group">
        <label>Категория:</label>
        <select v-model="category" required>
          <option v-for="cat in categories" :key="cat.id" :value="cat.id">
            {{ cat.name }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Дата:</label>
        <input v-model="date" type="date" required />
      </div>

      <div class="form-group">
        <label>Описание:</label>
        <textarea v-model="description"></textarea>
      </div>

      <button type="submit" class="submit-btn">Добавить</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const name = ref('');
    const amount = ref('');
    const category = ref('');
    const date = ref('');
    const description = ref('');
    const categories = ref([]);

    // Загружаем категории из БД
    const fetchCategories = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8001/api/categories/');
        const data = await response.json();
        categories.value = data;
      } catch (error) {
        console.error('Ошибка при загрузке категорий:', error);
      }
    };

    // Отправляем чек в БД
    const submitForm = async () => {
      try {
        const newCheck = {
          name: name.value,
          amount: parseFloat(amount.value),
          category_id: category.value,
          date: date.value,
          description: description.value,
        };

        const response = await fetch('http://127.0.0.1:8001/checks', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newCheck),
        });

        if (response.ok) {
          console.log('Чек добавлен!');
          name.value = '';
          amount.value = '';
          category.value = '';
          date.value = '';
          description.value = '';
        } else {
          console.error('Ошибка при добавлении чека');
        }
      } catch (error) {
        console.error('Ошибка:', error);
      }
    };

    onMounted(fetchCategories);

    return { name, amount, category, date, description, categories, submitForm };
  }
};
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

input, select, textarea {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

textarea {
  resize: vertical;
  min-height: 80px;
}

.submit-btn {
  width: 100%;
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-btn:hover {
  background: #0056b3;
}
</style>
