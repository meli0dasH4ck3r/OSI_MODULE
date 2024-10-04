class ApplicationLayer:
    def process_data(self, data):
        print(f"Application Layer: Processing data: {data}")
        return f"Processed({data})"

    def show_data(self, data):
        print(f"Application Layer: Showing data: {data}")
