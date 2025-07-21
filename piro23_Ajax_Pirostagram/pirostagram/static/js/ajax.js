
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".like-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const postId = btn.closest(".post").dataset.postId;

      fetch("/like/", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `post_id=${postId}`,
      })
        .then((res) => res.json())
        .then((data) => {
          btn.querySelector(".like-count").textContent = data.like_count;
          btn.classList.toggle("liked", data.liked);
        });
    });
  });

  document.querySelectorAll(".comment-form").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const postId = form.closest(".post").dataset.postId;
      const input = form.querySelector("input[name='text']");
      const text = input.value;

      fetch("/comment/add/", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `post_id=${postId}&text=${text}`,
      })
        .then((res) => res.json())
        .then((data) => {
          const li = document.createElement("li");
          li.setAttribute("data-comment-id", data.id);
          li.innerHTML = `${data.author}: ${data.text} <button class="delete-comment-btn">삭제</button>`;
          form.previousElementSibling.appendChild(li);
          input.value = "";
        });
    });
  });

  document.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-comment-btn")) {
      const li = e.target.closest("li");
      const commentId = li.dataset.commentId;

      fetch("/comment/delete/", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `comment_id=${commentId}`,
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.deleted) li.remove();
        });
    }
  });
});

// CSRF 토큰 쿠키에서 가져오기
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}
