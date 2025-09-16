"use client";
import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-blue-600 text-white px-6 py-4 flex justify-between items-center shadow-md">
      <h1 className="text-xl font-bold">ACT_PI_PAP</h1>
      <div className="space-x-6">
        <Link href="/" className="hover:underline">Inicio</Link>
        <Link href="/cars" className="hover:underline">Autos</Link>
        <Link href="/services" className="hover:underline">Servicios</Link>
        <Link href="/contact" className="hover:underline">Contacto</Link>
      </div>
    </nav>
  );
}
