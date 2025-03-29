import {Streamlit, withStreamlitConnection,} from "streamlit-component-lib"
import React, { useEffect } from "react"
import Plot from "react-plotly.js"
import { Data, Layout } from "plotly.js";

// interface to enforce args
interface Props {
  args: {
    data: Data[];
    layout: Layout;
  };
}

/**
 * Crossfit scatter plot of weight vs deadlift
 */
const CrossfitScatterPlot: React.FC<Props> = ({args}) => {
  // Set the component height
  useEffect(() => {
    Streamlit.setFrameHeight(500)
  }, [])

  const handleClick = (clickData: any) => {
    if (clickData.points && clickData.points.length > 0) {
      const point = clickData.points[0];
      const athleteName = point.text || `Athlete at index ${point.pointIndex}`;
      Streamlit.setComponentValue({
        series: point.curveNumber,
        pointIndex: point.pointIndex,
        x: point.x,
        y: point.y,
        athleteName: athleteName  // Send back the athlete name
      })
    }
  }
  
  return (
    <div style={{ width: '100%' }}>
      {args.data && args.layout ? (
        <Plot
          data={args.data}
          layout={args.layout}
          style={{ width: '100%', height: '450px' }}
          onClick={handleClick}
          config={{ responsive: true }}
        />
      ) : (
        <div style={{
          width: '100%', 
          height: '450px',
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'center',
          backgroundColor: '#f8f9fa', 
          borderRadius: '4px'
        }}>
          <p>Waiting for data...</p>
        </div>
      )}
    </div>
  );
};

export default withStreamlitConnection(CrossfitScatterPlot);