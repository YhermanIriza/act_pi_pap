import Link from "next/link";

export default function HomePage() {
  return (
    <section className="px-6 md:px-16 lg:px-32 py-12">
      {/* Hero */}
      <div className="bg-gradient-to-r from-blue-600 to-blue-500 text-white p-16 rounded-3xl text-center shadow-lg">
        <h1 className="text-4xl md:text-5xl font-extrabold">
          Bienvenido a <span className="text-yellow-300">ACT_PI_PAP</span>
        </h1>
        <p className="mt-4 text-lg md:text-xl">
          Compra y vende autos fácilmente con nosotros 
        </p>

        {/* Botón con Link */}
        <Link href="/cars/">
          <button className="mt-8 bg-white text-blue-600 px-8 py-3 rounded-xl font-semibold hover:bg-gray-100 transition">
            Explorar autos
          </button>
        </Link>
      </div>
    </section>
  );
}
