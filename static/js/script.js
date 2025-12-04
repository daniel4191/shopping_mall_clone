document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.querySelector('.search-bar input');
  const dropdown = document.querySelector('#searchDropdown');

  // 1. 검색창 클릭(포커스) 시 드롭다운 열기
  searchInput.addEventListener('focus', () => {
    dropdown.classList.add('active');
  });

  // 2. 바깥 영역 클릭 시 드롭다운 닫기
  document.addEventListener('click', e => {
    // 클릭한 대상이 검색창 내부나 드롭다운 내부가 아니라면 닫음
    const isClickInside =
      searchInput.closest('.search-bar').contains(e.target) ||
      dropdown.contains(e.target);

    if (!isClickInside) {
      dropdown.classList.remove('active');
    }
  });
});

document.addEventListener('DOMContentLoaded', function () {
  // 메인 배너 슬라이드 설정
  var swiper = new Swiper('.mySwiper', {
    loop: true, // 무한 반복
    autoplay: {
      // 자동 재생 설정
      delay: 3000, // 3초마다 넘어감
      disableOnInteraction: false
    },
    pagination: {
      // 하단 점 표시
      el: '.swiper-pagination',
      clickable: true
    }
  });
});
