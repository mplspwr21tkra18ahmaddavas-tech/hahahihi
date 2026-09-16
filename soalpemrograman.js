// 1. Membalikkan kalimat
function balikKalimat(str) {
  return str.split('').reverse().join('');
}

// 2. Cari huruf dan hitung jumlahnya
function hitungHuruf(str, target) {
  let count = 0;
  for (let char of str) {
    if (char.toLowerCase() === target.toLowerCase()) count++;
  }
  return count;
}

// 3. Hitung total karakter
function hitungKarakter(str) {
  return str.length;
}
// 4. "122333444455555666666"
function pola4() {
  let res = '';
  for (let i = 1; i <= 6; i++) res += String(i).repeat(i);
  return res;
}

// 5. "666666555554444333221"
function pola5() {
  let res = '';
  for (let i = 6; i >= 1; i--) res += String(i).repeat(i);
  return res;
}

// 6. "112123123412345123456"
function pola6() {
  let res = '', temp = '';
  for (let i = 1; i <= 6; i++) {
    temp += i;
    res += temp;
  }
  return res;
}

// 7. "654321543214321321211"
function pola7() {
  let res = '';
  for (let i = 6; i >= 1; i--) {
    for (let j = i; j >= 1; j--) res += j;
  }
  return res;
}

// 8. "112333123455555123456" (Pola bergantian: ganjil repeat, genap deret)
function pola8() {
  let res = '', temp = '';
  for (let i = 1; i <= 6; i++) {
    temp += i;
    if (i % 2 !== 0) res += String(i).repeat(i);
    else res += temp;
  }
  return res;
}

// 9. "122123444412345666666" (Genap repeat, ganjil deret)
function pola9() {
  let res = '', temp = '';
  for (let i = 1; i <= 6; i++) {
    temp += i;
    if (i % 2 === 0) res += String(i).repeat(i);
    else res += temp;
  }
  return res;
}

// 10. "654321555554321333211"
function pola10() {
  let res = '';
  for (let i = 6; i >= 1; i--) {
    if (i % 2 === 0) {
      for (let j = i; j >= 1; j--) res += j;
    } else {
      res += String(i).repeat(i);
    }
  }
  return res;
}

// 11. "666666123454444123221"
function pola11() {
  let res = '';
  for (let i = 6; i >= 1; i--) {
    if (i % 2 === 0) {
      res += String(i).repeat(i);
    } else {
      for (let j = 1; j <= i; j++) res += j;
    }
  }
  return res;
}

// 12. Generasi pola berulang berselang sampai batas n
function pola12(max = 9) {
  let res = '', temp = '';
  for (let i = 1; i <= max; i++) {
    temp += i;
    if (i % 2 === 0) res += String(i).repeat(i);
    else res += temp;
  }
  return res;
}

// 13. Generasi pola berulang berselang sampai batas n
function pola13(max = 9) {
  let res = '', temp = '';
  for (let i = 1; i <= max; i++) {
    temp += i;
    if (i % 3 === 0) res += temp;
    else res += String(i).repeat(i);
  }
  return res;
}

// 14. "888888887777777654321543214444333211"
function pola14() {
  let res = '';
  for (let i = 8; i >= 1; i--) {
    if (i === 6 || i === 5 || i === 2) {
      for (let j = i; j >= 1; j--) res += j;
    } else {
      res += String(i).repeat(i);
    }
  }
  return res;
}

// 15. "876543217654321666666555554321321221"
function pola15() {
  let res = '';
  const deretList = [8, 7, 4, 3];
  for (let i = 8; i >= 1; i--) {
    if (deretList.includes(i)) {
      for (let j = i; j >= 1; j--) res += j;
    } else {
      res += String(i).repeat(i);
    }
  }
  return res;
}
// 16. Pattern: +4, -2
function deret16(length = 10) {
  let res = [1];
  for (let i = 1; i < length; i++) {
    let prev = res[i - 1];
    res.push(i % 2 !== 0 ? prev + 4 : prev - 2);
  }
  return res.join(' ');
}

// 17. Pattern: +10, -5
function deret17(length = 10) {
  let res = [2];
  for (let i = 1; i < length; i++) {
    let prev = res[i - 1];
    res.push(i % 2 !== 0 ? prev + 10 : prev - 5);
  }
  return res.join(' ');
}

// 18. Pattern: -3, +5
function deret18(length = 10) {
  let res = [5];
  for (let i = 1; i < length; i++) {
    let prev = res[i - 1];
    res.push(i % 2 !== 0 ? prev - 3 : prev + 5);
  }
  return res.join(' ');
}

// 19. Pattern: *3, -5
function deret19(length = 10) {
  let res = [3];
  for (let i = 1; i < length; i++) {
    let prev = res[i - 1];
    res.push(i % 2 !== 0 ? prev * 3 : prev - 5);
  }
  return res.join(' ');
}

// 20. Pattern: +1, +2, +1, +3... (+1, +2, +1, +3 berulang)
function deret20(length = 13) {
  let res = [1];
  let step = [1, 2, 1, 3];
  for (let i = 1; i < length; i++) {
    res.push(res[i - 1] + step[(i - 1) % step.length]);
  }
  return res.join(' ');
}

// 21. Geometric: x2 (1 2 4 8 16 32 64 128 256 512)
function deret21(length = 10) {
  let res = [];
  for (let i = 0; i < length; i++) {
    res.push(Math.pow(2, i));
  }
  return res.join(' ');
}
// 22. Faktorial n!
function faktorial(n) {
  let hasil = 1;
  let proses = [];
  for (let i = n; i >= 1; i--) {
    hasil *= i;
    proses.push(i);
  }
  return `${n}! = ${proses.join('x')} = ${hasil}`;
}

// 23. Fibonacci hingga nilai maksimum
function fibonacci(max) {
  let res = [0, 1];
  while (true) {
    let next = res[res.length - 1] + res[res.length - 2];
    if (next > max) break;
    res.push(next);
  }
  return res.join(', ');
}
// ==========================================
// HELPER FUNGSIONAL (Tahun Kabisat & Kelipatan)
// ==========================================

// Cek apakah suatu tahun adalah tahun kabisat
function isKabisat(tahun) {
  return (tahun % 4 === 0 && tahun % 100 !== 0) || (tahun % 400 === 0);
}

// Fungsi utama untuk filter tahun kabisat berdasarkan digit terakhir
function filterKabisat(nAwal, nAkhir, digitTerakhir) {
  let hasil = [];
  for (let y = nAwal; y <= nAkhir; y++) {
    if (isKabisat(y) && y % 10 === digitTerakhir) {
      hasil.push(y);
    }
  }
  return hasil;
}

// Fungsi utama untuk filter bilangan yang habis dibagi X
function habisDibagi(nAwal, nAkhir, pembagi) {
  let hasil = [];
  for (let i = nAwal; i <= nAkhir; i++) {
    if (i % pembagi === 0) {
      hasil.push(i);
    }
  }
  return hasil;
}

// ==========================================
// IMPLEMENTASI 
// ==========================================

// 24. Kabisat dari n_awal hingga n_akhir yang angka terakhirnya 0
function soal24(nAwal, nAkhir) {
  return filterKabisat(nAwal, nAkhir, 0);
}

// 25. Kabisat dari n_awal hingga n_akhir yang angka terakhirnya 2
function soal25(nAwal, nAkhir) {
  return filterKabisat(nAwal, nAkhir, 2);
}

// 26. Kabisat dari n_awal hingga n_akhir yang angka terakhirnya 4
function soal26(nAwal, nAkhir) {
  return filterKabisat(nAwal, nAkhir, 4);
}

// 27. Kabisat dari n_awal hingga n_akhir yang angka terakhirnya 6
function soal27(nAwal, nAkhir) {
  return filterKabisat(nAwal, nAkhir, 6);
}

// 28. Kabisat dari n_awal hingga n_akhir yang angka terakhirnya 8
function soal28(nAwal, nAkhir) {
  return filterKabisat(nAwal, nAkhir, 8);
}

// 29. Bilangan yang habis dibagi 3 dari n_awal hingga n_akhir
function soal29(nAwal, nAkhir) {
  return habisDibagi(nAwal, nAkhir, 3);
}

// 30. Bilangan yang habis dibagi 4 dari n_awal hingga n_akhir
function soal30(nAwal, nAkhir) {
  return habisDibagi(nAwal, nAkhir, 4);
}

// 31. Bilangan yang habis dibagi 5 dari n_awal hingga n_akhir
function soal31(nAwal, nAkhir) {
  return habisDibagi(nAwal, nAkhir, 5);
}

// 32. Bilangan yang habis dibagi 6 dari n_awal hingga n_akhir
function soal32(nAwal, nAkhir) {
  return habisDibagi(nAwal, nAkhir, 6);
}

// 33. Bilangan yang habis dibagi 7 dari n_awal hingga n_akhir
function soal33(nAwal, nAkhir) {
  return habisDibagi(nAwal, nAkhir, 7);
}







// Helper fungsi delay untuk animasi CLI
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// Contoh template animasi (misal: Pojok Kiri Atas ke Kanan Atas dan kembali)
async function animasi35(width = 20, speed = 100) {
  // Bergerak dari kiri ke kanan
  for (let i = 0; i < width; i++) {
    console.clear();
    console.log(' '.repeat(i) + '0');
    await sleep(speed);
  }
  // Kembali dari kanan ke kiri
  for (let i = width - 1; i >= 0; i--) {
    console.clear();
    console.log(' '.repeat(i) + '0');
    await sleep(speed);
  }
}










// ==========================================
// KUMPULAN FUNGSI 
// ==========================================

// 42. Cari bilangan terbesar dari array angka (min 10 angka)
function soal42(arr) {
  return Math.max(...arr);
}

// 43. Cari bilangan terkecil dari array angka (min 10 angka)
function soal43(arr) {
  return Math.min(...arr);
}

// 44. Hitung JUMLAH BANYAKNYA bilangan genap dari array input
function soal44(arr) {
  return arr.filter(num => num % 2 === 0).length;
}

// 45. Hitung JUMLAH BANYAKNYA bilangan ganjil dari array input
function soal45(arr) {
  return arr.filter(num => num % 2 !== 0).length;
}

// 46. Total penjumlahan (SUM) bilangan bulat positif dari n_awal s/d n_akhir
function soal46(nAwal, nAkhir) {
  let total = 0;
  let awalPositif = Math.max(1, nAwal);
  for (let i = awalPositif; i <= nAkhir; i++) {
    total += i;
  }
  return total;
}

// 47. Total penjumlahan (SUM) bilangan genap dari n_awal s/d n_akhir
function soal47(nAwal, nAkhir) {
  let total = 0;
  for (let i = nAwal; i <= nAkhir; i++) {
    if (i % 2 === 0) total += i;
  }
  return total;
}

// 48. Total penjumlahan (SUM) bilangan ganjil dari n_awal s/d n_akhir
function soal48(nAwal, nAkhir) {
  let total = 0;
  for (let i = nAwal; i <= nAkhir; i++) {
    if (i % 2 !== 0) total += i;
  }
  return total;
}

// Helper untuk mengecek apakah sebuah angka adalah bilangan prima
function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

// 49. Tampilkan daftar bilangan Prima dari n_awal s/d n_akhir
function soal49(nAwal, nAkhir) {
  let hasil = [];
  for (let i = nAwal; i <= nAkhir; i++) {
    if (isPrime(i)) hasil.push(i);
  }
  return hasil;
}

// 50. Menghitung TOTAL SUM (penjumlahan) semua bilangan Prima dari n_awal s/d n_akhir
function soal50(nAwal, nAkhir) {
  let daftarPrima = soal49(nAwal, nAkhir);
  return daftarPrima.reduce((total, num) => total + num, 0);
}


// Contoh Formasi Matriks (Format 7x7)

// Formasi Diagonal / Garis (Modifikasi Karakter '0' dan '*')
function cetakFormasiDiagonal(n = 7) {
  for (let i = 0; i < n; i++) {
    let row = '';
    for (let j = 0; j < n; j++) {
      if (i === j) row += '*';
      else row += '0';
    }
    console.log(row);
  }
}

// Formasi Segitiga Terbalik
function cetakFormasiSegitiga(n = 7) {
  for (let i = 0; i < n; i++) {
    let row = '0'.repeat(i) + '*'.repeat(n - i);
    console.log(row);
  }
}


// Memanggil dan mencetak hasil
console.log(balikKalimat("Hallo")); // Output: ollaH
console.log(hitungHuruf("Algoritma", "a")); // Output: 2
console.log(hitungKarakter("Pemrograman")); // Output: 11
console.log(pola4()); // Output: 122333444455555666666
console.log(pola5()); // Output: 666666555554444333221
console.log(pola6());
console.log(pola7());
console.log(pola8());
console.log(pola9());
console.log(pola10());
console.log(pola11());
console.log(pola12());
console.log(pola13());
console.log(pola14());
console.log(pola15());
console.log(deret16());
console.log(deret17());
console.log(deret18());
console.log(deret19());
console.log(deret20());
console.log(deret21());
console.log(faktorial(3));
console.log(fibonacci(35));
// Contoh rentang tahun: 1900 hingga 2024
console.log("24. Kabisat ekor 0 (1900-2024):", soal24(1900, 2024));
console.log("25. Kabisat ekor 2 (1900-2024):", soal25(1900, 2024));
console.log("26. Kabisat ekor 4 (1900-2024):", soal26(1900, 2024));
console.log("27. Kabisat ekor 6 (1900-2024):", soal27(1900, 2024));
console.log("28. Kabisat ekor 8 (1900-2024):", soal28(1900, 2024));

// Contoh rentang angka: 1 hingga 30
console.log("29. Habis dibagi 3 (1-30):", soal29(1, 30));
console.log("30. Habis dibagi 4 (1-30):", soal30(1, 30));
console.log("31. Habis dibagi 5 (1-30):", soal31(1, 30));
console.log("32. Habis dibagi 6 (1-30):", soal32(1, 30));
console.log("33. Habis dibagi 7 (1-30):", soal33(1, 30));
// ==========================================
// EKSEKUSI & MENAMPILKAN HASIL
// ==========================================

// Data contoh untuk Soal 42 - 45 (10 angka acak)
const dataAngka = [12, 7, 45, 23, 88, 3, 64, 19, 90, 31];
console.log("Data Input (10 Angka):", dataAngka);
console.log("-----------------------------------------");

console.log("42. Bilangan Terbesar  :", soal42(dataAngka));
console.log("43. Bilangan Terkecil  :", soal43(dataAngka));
console.log("44. Banyak Bil. Genap  :", soal44(dataAngka));
console.log("45. Banyak Bil. Ganjil :", soal45(dataAngka));

console.log("\n--- Hasil Rentang Angka (1 s/d 10) ---");
console.log("46. Total Bulat Positif (1-10) :", soal46(1, 10)); // 1+2+3+...+10 = 55
console.log("47. Total Bilangan Genap (1-10):", soal47(1, 10)); // 2+4+6+8+10 = 30
console.log("48. Total Bilangan Ganjil(1-10):", soal48(1, 10)); // 1+3+5+7+9 = 25

console.log("\n--- Bilangan Prima (1 s/d 20) ---");
console.log("49. Daftar Prima (1-20)        :", soal49(1, 20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log("50. Total Sum Prima (1-20)     :", soal50(1, 20)); // 2+3+5+7+11+13+17+19 = 77

console.log(cetakFormasiDiagonal());
console.log(cetakFormasiSegitiga());


console.log(kontol)