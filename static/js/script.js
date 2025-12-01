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
