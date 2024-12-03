int return4() { 
  return 4; 
}

int suma(n, m) {
  return n + m;
}

int par(n) {
  if ((n % 2) == 0) { 
    return 1; 
  } else {
    return 0;
  }
}

int factorial(n) { 
  if (n == 0) { 
    return 1; 
  } else {
    return n * factorial (n - 1);
  }
}

int fibonacci(n) {
  if (n == 0) {
    return 0;
  } else { 
    if (n == 1) {
        return 1; 
      } else {
    }
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
  return fibonacci(5);
}