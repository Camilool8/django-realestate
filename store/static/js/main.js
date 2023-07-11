$(document).ready(function () {
  $(".partners-carousel").slick({
    slidesToShow: 3, // Number of slides to show
    slidesToScroll: 1, // Number of slides to scroll
    infinite: true, // Enable infinite scrolling
    autoplay: true, // Enable autoplay
    autoplaySpeed: 2000, // Autoplay interval in milliseconds
    responsive: [
      {
        breakpoint: 768, // Adjust this value based on your design
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 576, // Adjust this value based on your design
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });
});
