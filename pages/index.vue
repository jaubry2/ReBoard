<template>
    <div>
      <button @click="addProduct">Add Product</button>
      <h1>Bite</h1>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      test() {
        console.log("Test");
      },
      async addProduct() {
        console.log("Adding Product");
        try {
          const data = await fetch("api/create_product", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              url: "Test_URL",
              title: "Test_Title",
              price: 3,
              image_links: ["1", "2"],
              description: "Test_Description",
            }),
          });
          const response = await data.json();
          console.log(response);
        } catch (error) {
          console.error("Error adding product:", error);
        }
      },
    },
    mounted() {
      this.test(); // Appeler la méthode au montage si nécessaire
    },
  };
  </script>
  
  <style>
  /* Ajoutez votre style ici */
  </style>
  