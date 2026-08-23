import { Source } from "@/types/chat";

interface SourceCardProps {
  source: Source;
}

export default function SourceCard({
  source,
}: SourceCardProps) {
  return (
    <div className="rounded-xl border border-gray-200 bg-gray-50 p-4">
      <div className="flex items-start justify-between gap-4">

        <div>
          <p className="font-medium text-gray-900">
            {source.document}
          </p>

          <p className="mt-1 text-sm text-gray-600">
            Page {source.page}
          </p>
        </div>

        <span className="rounded-md bg-white px-2 py-1 text-xs font-medium text-gray-500">
          Source
        </span>

      </div>
    </div>
  );
}