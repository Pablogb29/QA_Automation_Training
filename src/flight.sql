BEGIN
  -- Paso 1: Reservar asientos libres
  UPDATE seats s
  JOIN requests r ON s.seat_no = r.seat_no
  SET s.status = 1,
      s.person_id = r.person_id
  WHERE r.request = 1
    AND s.status = 0;

  -- Paso 2: Comprar asientos libres
  UPDATE seats s
  JOIN requests r ON s.seat_no = r.seat_no
  SET s.status = 2,
      s.person_id = r.person_id
  WHERE r.request = 2
    AND s.status = 0;

  -- Paso 3: Comprar asientos reservados por la misma persona
  UPDATE seats s
  JOIN requests r ON s.seat_no = r.seat_no
  SET s.status = 2
  WHERE r.request = 2
    AND s.status = 1
    AND s.person_id = r.person_id;

  -- ✅ Mostrar los resultados finales
  SELECT * FROM seats ORDER BY seat_no;
END
