export default function Home() {
  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-gray-900">
        UK Politics Mobile App
      </h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Bills Section */}
        <section className="p-6 bg-white rounded-lg shadow">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            Parliamentary Bills
          </h2>
          <p className="text-gray-600">
            Track and monitor bills as they progress through Parliament
          </p>
        </section>

        {/* MPs Section */}
        <section className="p-6 bg-white rounded-lg shadow">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            MPs & Lords
          </h2>
          <p className="text-gray-600">
            View profiles, voting records, and activities of parliamentarians
          </p>
        </section>
      </div>
    </div>
  );
}