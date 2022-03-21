const posts = [
    { author: "add1", title: "Posf1" },
    { author: "add2", title: "Postf2" },
    { author: "add3", title: "Postf3" },
  ];
  const addPost = (newPost) => {
    return new Promise((resolve, reject) => {
      try {
        posts.push(newPost);
        resolve(posts);
      } catch (err) {
        reject(err);
      }
    });
  };
  
  const orderPost = () => {
    return new Promise((resolve, reject) => {
      if (posts.length > 0) {
        posts.map((post) => {
          console.log(post.title);
        });
        resolve("Veriler sıralandı.");
      } else {
        reject("Bir hata oluştu.");
      }
    });
  };
  
  async function bitir() {
    const newPost = { author: "test", title: "test22" };
    try {
      await orderPost();
      await addPost(newPost);
      await orderPost();
      console.log("İşlem başarılı.");
    } catch (error) {
      console.log(error);
    }
  }
  
  bitir();



