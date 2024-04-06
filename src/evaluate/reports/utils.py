import pandas as pd
import os


def add_new_results(cfg, report_df: pd.DataFrame, file_path: str = "report"):
    report_path = f'{cfg.save_path}/{file_path}.csv'

    if os.path.exists(report_path) and os.path.getsize(report_path) > 0:
        df = pd.read_csv(report_path)
        df = pd.concat([df, report_df], ignore_index=True)
    else:
        df = report_df
    
    df.to_csv(report_path, index=False)