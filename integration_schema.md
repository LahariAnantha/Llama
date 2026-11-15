# Data Integration Schema

## Overview

The project integrates three datasets that measure consumer prices, retail spending, and unemployment in the United States. Since all three datasets contain monthly observations, integration is performed using a common date attribute.

## Dataset Structures

### FRED CPI
- `date`: Monthly reporting date
- `cpi`: Consumer Price Index value

### Census MRTS
- `date`: Monthly reporting date
- `sales_millions`: Seasonally adjusted Retail Trade and Food Services sales in millions of dollars

### BLS Unemployment
- `date`: Monthly reporting date
- `unemployment_rate`: Seasonally adjusted civilian unemployment rate (%)

## Common Integration Attribute

The shared attribute is `date`, standardized to `YYYY-MM-DD` using the first day of each reporting month.

The expected relationship is one-to-one across datasets, with at most one observation per month in each cleaned dataset.

## Integration Method

The datasets will be integrated using Python's `pandas` library through an inner join on `date`.

This approach ensures that the resulting dataset includes only months with available observations for all three economic indicators.

The primary analysis period is January through December 2025, based on the selected retail data.

## Missing Data Handling

The unemployment dataset contains a missing value for October 2025. This observation was excluded during cleaning and therefore will not appear in the integrated dataset.

Based on the cleaned date coverage, the expected integrated dataset contains 11 monthly observations, subject to validation that the CPI series contains all corresponding months.

## Output

The resulting integrated dataset will be saved to:

`data/processed/integrated.csv`

The dataset will contain the standardized date, CPI, retail sales, and unemployment rate variables.

## Limitations

The integration process only retains complete observations, reducing the number of months available for analysis.

The limited time period restricts the strength of conclusions about broader economic trends. Results will be interpreted as exploratory associations rather than evidence of causation.