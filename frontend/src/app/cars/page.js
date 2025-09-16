"use client";

import { useEffect, useState } from "react";
import api from "../services/api";

export default function CarsPage() {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    api.get("/cars/")
      .then((res) => {
        setCars(res.data);
      })  
      .catch((err) => {
        console.error("Error al obtener autos:", err);
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Lista de Autos</h1>
      {cars.length === 0 ? (
        <p>No hay autos disponibles</p>
      ) : (
        <ul>
          {cars.map((car) => (
            <li key={car.id}>
              {car.name} - {car.model}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
