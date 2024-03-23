<template>
  <div class="container">
    <h2>Add Classroom</h2>
    <form class="form" @submit.prevent="addClassroom">
      <div class="form-group">
        <label for="location">Location:</label>
        <input type="text" id="location" v-model="location" class="form-control">
      </div>
      <div class="form-group">
        <label for="classroom_name">Classroom Name:</label>
        <input type="text" id="classroom_name" v-model="classroom_name" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Add Classroom</button>
    </form>
      <h2>Book Classroom</h2>
    <!-- Book Classroom form -->
    <form class="form" @submit.prevent="bookClassroom">
      <div class="form-group">
        <label for="classroom_id">Classroom:</label>
        <select v-model="selectedClassroomId" class="form-control">

          <option v-for="classroom in classrooms" :key="classroom.id" :value="classroom.id">{{ classroom.classroom_name }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="date">Date:</label>
        <input type="date" id="date" v-model="date" class="form-control">
      </div>
      <div class="form-group">
        <label for="purpose">Purpose:</label>
        <input type="text" id="purpose" v-model="purpose" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Book Classroom</button>
    </form>
  </div>
</template>

<style>
.container {

  width: 80%;
  border-radius: 20px;
  border: 1px solid #ccc;
  background-color: #2f2f2f;
  padding: 20px;
  position: absolute; /* or fixed */
  left: 1.5%;
  top: 5%;
}

.form {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="date"] {
  width: 100%;
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff; /* Blue color */
  color: #fff;
  cursor: pointer;
}

.btn:hover {
  background-color: #0056b3; /* Darker blue color on hover */
}
</style>



<script>
  import axios from 'axios';

export default {
  data() {
    return {
      classrooms: []  ,
      selectedClassroomId: null,
      date: '',
      purpose: '',
      location: '',
      classroom_name: '',
      date: '',
    };
  },
  mounted() {
    this.fetchClassrooms();
  },
  methods: {
    addClassroom() {
        axios.post('http://127.0.0.1:5000/classrooms', {
          location: this.location,
          classroom_name: this.classroom_name
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
      },
    fetchClassrooms() {
      axios.get('http://127.0.0.1:5000/classrooms')
        .then(response => {
          this.classrooms = response.data.classrooms
          console.log(this.classrooms)
        })
        .catch(error => {
          console.error(error);
        });
    },
    bookClassroom() {
        console.log(this.selectedClassroomId)
        console.log()
      axios.post('http://127.0.0.1:5000/bookings', {
        
        classroom_id: this.selectedClassroomId,
        date: this.date,
        purpose: this.purpose
      })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
    }
  }
};
</script>
