function applySort(value) {
  const url = new URL(window.location.href);
  url.searchParams.set('sort', value);
  url.searchParams.delete('page');
  window.location.href = url.toString();
}
