/**
 * API communication layer
 * Handles all fetch calls with error propagation.
 */
const API = (() => {
  const TIMEOUT_MS = 3000;

  async function fetchWithTimeout(url) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
    try {
        const res = await fetch(url, { signal: controller.signal });
        if (!res.ok) return null;  // 404면 null 반환
        return await res.json();
    } catch {
        return null;  // 에러나도 null 반환
    } finally {
        clearTimeout(timer);
    }
}

  return {
    getTreadmillData() {
      return fetchWithTimeout('/TMdata');
    },

    getTowelData() {
      return fetchWithTimeout('/toweldata');
    },

    getEquipmentData() {
      return fetchWithTimeout('/equipmentdata');
    },
  };
})();
