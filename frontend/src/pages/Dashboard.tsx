export default function Dashboard() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-gray-900 mb-8">
        Ads Dashboard Platform
      </h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-500 mb-2">Investimento</h3>
          <p className="text-3xl font-bold text-gray-900">R$ 45.2K</p>
          <p className="text-sm text-green-600 mt-2">↑ 12.5%</p>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-500 mb-2">Conversões</h3>
          <p className="text-3xl font-bold text-gray-900">1,234</p>
          <p className="text-sm text-green-600 mt-2">↑ 8.3%</p>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-500 mb-2">ROAS</h3>
          <p className="text-3xl font-bold text-gray-900">4.8x</p>
          <p className="text-sm text-green-600 mt-2">↑ 15.2%</p>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-500 mb-2">CPA</h3>
          <p className="text-3xl font-bold text-gray-900">R$ 36.60</p>
          <p className="text-sm text-red-600 mt-2">↓ 5.7%</p>
        </div>
      </div>
      
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">
          Performance Overview
        </h2>
        <p className="text-gray-600">
          Dashboard em desenvolvimento. Integre com as APIs do Google Ads e Meta Ads
          para visualizar métricas em tempo real.
        </p>
      </div>
    </div>
  )
}

